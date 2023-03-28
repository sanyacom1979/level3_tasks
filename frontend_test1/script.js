function getProducts() {
fetch("https://fakestoreapi.com/products")
            .then(res => res.json())
            .then(data => {
                //console.log(data)

                const products = document.getElementById("products")

                data.forEach(product => {
                    products.innerHTML = products.innerHTML.concat(
                        `<div class="product">
                            <p class="title">${product.title}</p>
                            <img class="image" src=${product.image} alt=""></img>
                            <div>
                                <p><b>${product.price}$</b></p>
                                <p class="description"><b>Описание:</b> ${product.description}</p>
                            </div>
                        </div>
                        `
                        )

                })

            })




}