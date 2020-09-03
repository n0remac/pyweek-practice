#version 330

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

in vec2 vf_uv;
in vec4 vf_color;
in float vf_solid_factor;

void main() {

    float distanceToLight = length(vf_uv);
    float falloff = 1.0 - distanceToLight;

    falloff = smoothstep(1.0,vf_solid_factor, distanceToLight);

    fragColor = max(vec4(0.0), vf_color * falloff);
}