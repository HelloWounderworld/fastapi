# Tip:
Query, Path e outras classes que você verá a frente são subclasses de uma classe comum Param.

Todas elas compartilham os mesmos parâmetros para validação adicional e metadados que você viu.

# Technical Detail:
Quando você importa Query, Path e outras de fastapi, elas são na verdade funções.

Que quando chamadas, retornam instâncias de classes de mesmo nome.

Então, você importa Query, que é uma função. E quando você a chama, ela retorna uma instância de uma classe também chamada Query.

Estas funções são assim (ao invés de apenas usar as classes diretamente) para que seu editor não acuse erros sobre seus tipos.

Dessa maneira você pode usar seu editor e ferramentas de desenvolvimento sem precisar adicionar configurações customizadas para ignorar estes erros.

# References:

1. [Param class. Query and Path are subclass of the Praram class][1]

[1]: https://param.holoviz.org/user_guide/How_Param_Works.html