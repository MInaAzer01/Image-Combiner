var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

let upload1 = document.querySelector('#image_input1')
let upload2 = document.querySelector('#image_input2')
let result1 = document.querySelector('#result1')
let result2 = document.querySelector('#result2')
let submit = document.getElementById("combine_btn")
let original_img_1 = ""
let original_img_2 = ""
let checkbox = document.getElementById("uniform-phase")
let checkbox2 = document.getElementById("uniform-Magnitude")
let options = document.getElementById("image1_info")
let image1_x1, image1_x2, image2_x1, image2_x2, image1_y1, image1_y2, image2_y1, image2_y2

checkbox.addEventListener('change', e=>{
  send()
})


upload1.addEventListener('change', e => {
  if (e.target.files.length) {
    // start file reader
    const reader = new FileReader();
    reader.onload = e => {
      if (e.target.result) {
        // create new image
        let img = document.createElement('img');
        img.id = 'image';
        img.src = e.target.result;
        // clean result before
        result1.innerHTML = '';
        // append new image
        result1.appendChild(img)
        // origial image
        original_img_1 = e.target.result

        // init cropper
        cropper1 = new Cropper(img, {
          zoomOnWheel: false,
          movable: false,
          guides: false,
          crop: function (e) {

            image1_x1 = e.detail.x

            image1_y1 = e.detail.y

            image1_x2 = e.detail.width + e.detail.x

            image1_y2 = e.detail.height + e.detail.y
            
            
          },
          cropend: function(e){
            send()
          }
        });
      }
    };
    reader.readAsDataURL(e.target.files[0]);
  }
});
checkbox2.addEventListener('change', e=>{
  send()
})

options.addEventListener('change',  e=>{
  send()
})

upload2.addEventListener('change', e => {
  if (e.target.files.length) {
    // start file reader
    const reader = new FileReader();
    reader.onload = e => {
      if (e.target.result) {
        // create new image
        let img2 = document.createElement('img');
        img2.id = 'image';
        img2.src = e.target.result;
        original_img_2 = e.target.result
        // clean result before
        result2.innerHTML = '';
        // append new image
        result2.appendChild(img2)
        // init cropper
        cropper2 = new Cropper(img2, {
          zoomOnWheel: false,
          movable: false,
          guides: false,
          crop: function (e) {
            image2_x1 = e.detail.x

            image2_y1 = e.detail.y

            image2_x2 = e.detail.width + e.detail.x

            image2_y2 = e.detail.height + e.detail.y
            
            

          },
          cropend: function(e){
            send()
          }
        });
      }
    };
    reader.readAsDataURL(e.target.files[0]);
  }
});


submit.addEventListener('click', e => {
  e.preventDefault();
  send()
}
)


function send(){
  
  // to handle if the user not enter two images
  try {
    const option = document.getElementById("image1_info");
    if (original_img_1 == "" || original_img_2 == "") {
      throw "error : not enought images "
    }
    checkbox_value = document.querySelector('#uniform-phase').checked;
    console.log(checkbox_value)
    checkbox_value_Magnitude = document.querySelector('#uniform-Magnitude').checked;

  
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5000/saveImg',
      data: {
        original_1: original_img_1,
        original_2: original_img_2,
        option: option.value,
        img1_x1: image1_x1,
        img1_x2: image1_x2,
        img1_y1: image1_y1,
        img1_y2: image1_y2,
        img2_x1: image2_x1,
        img2_x2: image2_x2,
        img2_y1: image2_y1,
        img2_y2: image2_y2,
        checkbox: checkbox_value,
        checkbox_Magnitude: checkbox_value_Magnitude
      },
      success: function (res) {
        var responce = JSON.parse(res)
        var big_cont = document.getElementById("images_container")
        const cont12 = document.getElementById("cont1")
        cont12.remove()
        var img_1 = document.createElement("div")
        img_1.className = "container"
        img_1.id = "cont1"
        img_1.innerHTML = responce[1]
        big_cont.appendChild(img_1)

      }


    })
  } catch (error) {
    console.log("please upload two images")
  }

  
}