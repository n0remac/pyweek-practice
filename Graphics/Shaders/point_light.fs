#version 330

//Distance from vertex shader
in vec2 v_distance;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

//Light color setting
uniform vec4 lightColor;
uniform float u_radius;

void main() {

    float distanceToLight = length(v_distance);
    float ultraJankFalloff = 1.0 - (distanceToLight / u_radius);

    fragColor = max(vec4(0.0), lightColor * ultraJankFalloff);
    //fragColor = vec4(1.0, 1.0, 1.0, 1.0);
}