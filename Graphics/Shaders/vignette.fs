#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_source;

uniform float u_start_distance;
uniform float u_end_distance;
uniform float u_strength;

uniform vec2 u_scale;


float saturate(float value){
    return clamp(value, 0.0, 1.0);
}

vec4 saturate(vec4 color){
    return clamp(vec4(0.0), vec4(1.0), color);
}

void main() {

    vec4 sourceColor = texture(t_source, v_uv);

    float fromCenter = length(u_scale * ((v_uv - 0.5f) * 2.0));

    float strength = smoothstep(u_start_distance, u_end_distance, fromCenter);

    strength = saturate(strength * u_strength);

    fragColor = mix(sourceColor, vec4(0.0), strength);
}