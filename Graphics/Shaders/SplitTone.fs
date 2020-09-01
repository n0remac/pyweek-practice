#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_source; 

uniform float u_threshold;
uniform float u_crossover_half;
uniform vec3 u_shadow_color;
uniform vec3 u_highlight_color;


void main() {

    vec3 sourceColor = texture(t_source, v_uv).xyz;

    //TODO:Real Luminance
    float luminance = length(sourceColor);
                                //TODO:Refactor this out of the shader and into SplitTone.py
    float lerpTime = smoothstep(u_threshold - u_crossover_half,u_threshold + u_crossover_half, luminance);
    vec3 splitToneColor = mix(u_shadow_color, u_highlight_color, lerpTime);

    vec3 finalColor = sourceColor + splitToneColor;

    fragColor = vec4(finalColor, 0.0);
}