#version 330

// Color passed in from the vertex shader
in vec2 v_uv;

// The pixel we are writing to in the framebuffer
out vec4 fragColor;

uniform float u_weight_count;
uniform float u_weights[45];

uniform float u_threshold;

uniform vec2 u_pixel_size_uv;

uniform sampler2D t_source; 

void main() {
    //For 7 taps, this is 3, which gives 3 left of current pixel, 3 right of current pixel and the current pixel
    int half_weight_count = int(u_weight_count)/2;
    //offset the start position to line up with the weight at index 0 in u_weights
    vec2 samplePos = v_uv;
    samplePos.x -= half_weight_count * u_pixel_size_uv.x;

    vec3 totalBloom = vec3(0.0);

    for(int i = 0; i < u_weight_count;i++)
    {
        vec3 sample = texture(t_source ,samplePos).xyz;

        //Subtract threshold and clip, will not affect final image if clipped to zero
        sample = max(vec3(0.0), sample - u_threshold);

        //multiply sample with gaussian weight
        totalBloom += sample * u_weights[i];
        //Increment sample position by one pixel/texel
        samplePos.x += u_pixel_size_uv.x;

    }

    fragColor = vec4(totalBloom, 1.0);
}