function addProductToOrder(productId){
    const productCount =$('#productCount').val();
    $.get('/order/add-to-cart?product_id='+productId+'&product_count='+productCount).then(res =>{
        Swal.fire({
            title:"اعلان",
            text:res.text,
            icon:res.icon,
            showCancelButton:false,
            confirmButtonColor:"#3085d6",
            cancelButtonColor:"#d33",
            confirmButtonText:res.confirm_button_text
        }).then((result) =>{
            if(result.isConfirmed && res.status === 'not_auth'){
                window.location.href='/login/';
            }else if(result.isConfirmed && res.status === 'success'){
                window.location.href='/order/user-basket';
            };
        });
    });
}