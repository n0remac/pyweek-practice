#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D srcTexture; 

void main() {

    fragColor = texture(srcTexture, v_uv);
}