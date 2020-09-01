#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_source;

uniform float u_strength;

void main() {

    vec3 result = vec3(
        texture(t_source, v_uv - vec2(u_strength, 0.0)).r,
        texture(t_source, v_uv).g,
        texture(t_source, v_uv + vec2(u_strength, 0.0)).b
    );

    fragColor = vec4(result, 1.0);
}