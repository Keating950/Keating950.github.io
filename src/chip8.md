---
title: CHIP-8 emulator
image_html: <img class="post_img" src="media/chip8.gif">
bar_order: 3
---
	
<p class="main_text">
In the summer of 2020, I wrote a <a href="https://github.com/Keating950/chip8">CHIP-8 emulator</a> in C. Inspired by
Mathew Zaleski's disseration
"<a href="http://www.cs.toronto.edu/~matz/dissertation/matzDissertation-latex2html/node6.html">YETI: a graduallY Extensible Trace Interpreter</a>,"
I wrote the main emulation loop in a threaded-interpreter style, which reduces
function call overhead in the host machine. The result is efficient, typically
O(1) dispatch of virtual instructions. The emulator requires only the <a
href="https://libsdl.org/download-2.0.php">SDL2</a> library to build and is
fully cross-platform compatible.
</p>
