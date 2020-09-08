#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_source; 
uniform float u_strength;





vec3 sample_lut(vec3 color, sampler2D lut)


void main() {

    vec4 sourceColor = texture(t_source, v_uv);
    fragColor = vec4(1.0) - sourceColor * u_strength;
}