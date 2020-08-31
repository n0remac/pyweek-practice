#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_source; 

void main() {

    vec4 hdrColor = texture(t_source, v_uv);

    //Reinhard tonemapping, basic but works good enough for this
    vec4 ldrColor = hdrColor / (1.0 + hdrColor);
    fragColor = ldrColor;
}