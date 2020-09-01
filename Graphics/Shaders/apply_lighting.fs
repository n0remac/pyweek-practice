#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform sampler2D t_Source; 
uniform sampler2D t_LightBuffer; 

void main() {

    //Load rendered sprite colors and light color from buffers
    vec4 sourceColor = texture(t_Source, v_uv);
    vec4 lightColor = texture(t_LightBuffer, v_uv);

    //Compute final HDR light color
    vec4 hdrColor = sourceColor * lightColor;//TODO:Do we need to do 1/PI for albedo in this context?

    //Tonemap to LDR //TODO:Move this after some bloom for extra spice
    //Reinhard tonemapping, basic but works good enough for this
    vec4 ldrColor = hdrColor / (1.0 + hdrColor);

    fragColor = ldrColor;
}