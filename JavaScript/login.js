function logar(){
    var login= document.getElementById('login').value;
    var senha=document.getElementById('senha').value;

    if(login== "admin" && senha=="123"){
        alert('Sucesso!')
        location.href='home.html';
    }else{
        alert('Valores atribuidos incorretos!')
    }

}