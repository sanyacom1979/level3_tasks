function getProducts() {
fetch("https://fakestoreapi.com/products")
            .then(res => res.json())
            .then(data => {
                
                const products = document.getElementById("products")
            
                data.forEach(product => {
                    products.innerHTML = products.innerHTML.concat(
                        `<div class="product"> 
                            <p class="title">${product.title}</p>
                            <img class="image" src="${product.image}" alt=""
                            <div>
                            <p><b>${product.price}$</b></p>
                            <p class="description">${product.description}</p>
                            </div>
                        </div>`
                        )
                })

            })

}