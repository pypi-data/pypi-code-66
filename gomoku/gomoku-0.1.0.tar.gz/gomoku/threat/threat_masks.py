'''
Masks to optimize threat search.
When looking for horizontal/main diagonal/off diagonal threats, certain positions should be ignored.
For example, when looking for a horizontal threat of length 5, only these starting positions should be considered:
______________________________
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -
|o o o o o o o o o o o - - - -

And when looking for off-diagonal threats, only these starting positions should be considered:
______________________________
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - o o o o o o o o o o o
|- - - - - - - - - - - - - - -
|- - - - - - - - - - - - - - -
|- - - - - - - - - - - - - - -
|- - - - - - - - - - - - - - -
'''
threat_mask = {
    5: {
        1: 3368450625791641569852801897221545090422390492443040367981145065471,
        14: 46746643025836220467672558992765845109795687268336,
        15: 53919893334301279589334030174039261347274288845081144962207220498431,
        16: 2921665189114763779229534937047865319362230454271,
    },
    6: {
        1: 1683402535507986969203427621327621215193993880688436881506942551039,
        14: 1425897411066692180130132434946704696329404384,
        15: 53919893334301279589334030174039261347274288845081144962207220498431,
        16: 44559294095834130629066638592084521760293887,
    },
    7: {
        1: 840878490366159668878740483380659277579795574811135138269841293823,
        14: 43472399046484070960588213894021854035904,
        15: 53919893334301279589334030174039261347274288845081144962207220498431,
        16: 679256235101313608759190842094091469311,
    }
}
