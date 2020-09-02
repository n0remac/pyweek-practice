#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform int u_weight_count;
uniform float u_weights[15];

uniform float u_power;

uniform vec2 u_pixel_size_uv;

uniform sampler2D t_source; 
uniform sampler2D t_xblur; 

void main() {
    //For 7 taps, this is 3, which gives 3 left of current pixel, 3 right of current pixel and the current pixel
    int half_weight_count = u_weight_count/2;
    //offset the start position to line up with the weight at index 0 in u_weights
    vec2 samplePos = v_uv;
    samplePos.y -= half_weight_count * u_pixel_size_uv.y;

    vec3 totalBloom = vec3(0.0);

    for(int i = 0; i < u_weight_count;i++)
    {
                            //On this pass, sample the image that is already blurred along the x axis
        vec3 sample = texture(t_xblur ,samplePos).xyz;

        //Note that we do not need to use the threshold here, that step was already done. doing it again will make the bloom ultra dark

        //multiply sample with gaussian weight
        totalBloom += sample * u_weights[i];

        //Increment sample position by one pixel/texel
        samplePos.y += u_pixel_size_uv.y;
    }

    //Read the original image
    vec4 originalImage = texture(t_source, v_uv);
    //Combine with blurred bloom, multiply power in here
    vec4 finalImage = originalImage + vec4(totalBloom * u_power, 0.0);

    fragColor = finalImage;
}