import re

with open(r'E:\Yuvan portfolio12\portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove text at the top
content = re.sub(r'^.*?<!DOCTYPE html>', '<!DOCTYPE html>', content, flags=re.DOTALL)

# 2. Remove text at the bottom
content = re.sub(r'debug the code without single error\s*$', '', content, flags=re.DOTALL)

# 3. Extract styles
style_match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    # Add new utility classes
    css_content += '\n\n/* Utility classes for removed inline styles */\n'
    css_content += '#termOutput { transition: opacity 0.4s ease; }\n'
    css_content += '.mt-8 { margin-top: 8px; }\n'
    css_content += '#termCursor { display: none; }\n'
    css_content += '.mb-0 { margin-bottom: 0; }\n'
    css_content += '.align-self-start { align-self: flex-start; }\n'
    css_content += '.text-green { color: var(--green); }\n'
    
    with open(r'E:\Yuvan portfolio12\style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    content = content.replace(style_match.group(0), '<link rel="stylesheet" href="style.css">')

# 4. Add rel="noopener noreferrer"
content = re.sub(r'target="_blank"(?!\s+rel=)', 'target="_blank" rel="noopener noreferrer"', content)

# 5. Fix inline styles
content = content.replace('style="opacity:0; transition:opacity 0.4s ease;"', '')
content = content.replace('class="terminal-line" style="margin-top:8px"', 'class="terminal-line mt-8"')
content = content.replace('class="cursor-blink" id="termCursor" style="display:none;"', 'class="cursor-blink" id="termCursor"')

content = content.replace('class="project-desc" style="margin-bottom:0"', 'class="project-desc mb-0"')
content = content.replace('class="btn btn-primary" onclick="handleForm()" style="align-self:flex-start;"', 'class="btn btn-primary align-self-start" onclick="handleForm()"')
content = content.replace('<span style="color:var(--green)">', '<span class="text-green">')

# Fix terminal JS to hide output initially
js_old = """        (async function playTerminal() {
            const cmdEl = document.getElementById('termCmd');
            const outputEl = document.getElementById('termOutput');
            const blinkEl = document.getElementById('termCursor');
            if (!cmdEl || !outputEl) return;
            try {"""
js_new = """        (async function playTerminal() {
            const cmdEl = document.getElementById('termCmd');
            const outputEl = document.getElementById('termOutput');
            const blinkEl = document.getElementById('termCursor');
            if (!cmdEl || !outputEl) return;
            outputEl.style.opacity = '0';
            try {"""
content = content.replace(js_old, js_new)

# Fix cursor animation JS
js_anim_old = """        // FIX 5: only activate custom cursor on real pointer/hover devices (not mobile)
        if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
            const cursor = document.getElementById('cursor');
            const ring = document.getElementById('cursorRing');
            if (cursor && ring) {
                cursor.style.display = 'block';
                ring.style.display = 'block';
                let mx = 0, my = 0, rx = 0, ry = 0;
                document.addEventListener('mousemove', e => {
                    mx = e.clientX; my = e.clientY;
                    cursor.style.left = mx + 'px'; cursor.style.top = my + 'px';
                });
                // FIX 3: animateRing at top-level scope, not buried inside another if block
                (function animateRing() {
                    rx += (mx - rx) * 0.12; ry += (my - ry) * 0.12;
                    ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
                    requestAnimationFrame(animateRing);
                })();
                document.querySelectorAll('a, button, .skill-pill').forEach(el => {
                    el.addEventListener('mouseenter', () => { ring.style.transform = 'translate(-50%,-50%) scale(1.8)'; ring.style.borderColor = 'rgba(0,255,136,0.6)'; });
                    el.addEventListener('mouseleave', () => { ring.style.transform = 'translate(-50%,-50%) scale(1)'; ring.style.borderColor = 'rgba(0,255,136,0.4)'; });
                });
            }
        }"""

js_anim_new = """        let mx = 0, my = 0, rx = 0, ry = 0;
        let cursorRing = null;

        // FIX 3: animateRing at top-level scope, not buried inside another if block
        function animateRing() {
            if (cursorRing) {
                rx += (mx - rx) * 0.12; ry += (my - ry) * 0.12;
                cursorRing.style.left = rx + 'px'; cursorRing.style.top = ry + 'px';
            }
            requestAnimationFrame(animateRing);
        }
        requestAnimationFrame(animateRing);

        // FIX 5: only activate custom cursor on real pointer/hover devices (not mobile)
        if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
            const cursor = document.getElementById('cursor');
            const ring = document.getElementById('cursorRing');
            if (cursor && ring) {
                cursorRing = ring;
                cursor.style.display = 'block';
                ring.style.display = 'block';
                document.addEventListener('mousemove', e => {
                    mx = e.clientX; my = e.clientY;
                    cursor.style.left = mx + 'px'; cursor.style.top = my + 'px';
                });
                document.querySelectorAll('a, button, .skill-pill').forEach(el => {
                    el.addEventListener('mouseenter', () => { ring.style.transform = 'translate(-50%,-50%) scale(1.8)'; ring.style.borderColor = 'rgba(0,255,136,0.6)'; });
                    el.addEventListener('mouseleave', () => { ring.style.transform = 'translate(-50%,-50%) scale(1)'; ring.style.borderColor = 'rgba(0,255,136,0.4)'; });
                });
            }
        }"""
content = content.replace(js_anim_old, js_anim_new)

with open(r'E:\Yuvan portfolio12\portfolio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
