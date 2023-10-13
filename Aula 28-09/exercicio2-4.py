"""
Um bloco try e catch contém varios “catches”. Explique como e por que isso as vezes acontece.

Em Python, a estrutura de tratamento de exceções utiliza try, except e opcionalmente finally.
Ao contrário de algumas outras linguagens de programação, Python não suporta múltiplos blocos catch.
Em vez disso, você pode usar múltos except dentro do mesmo bloco try para lidar com diferentes tipos de exceções.

O motivo para ter múltiplos blocos except é permitir que você trate diferentes tipos de exceções de forma separada
e específica, conforme necessário para o seu programa. Cada tipo de exceção pode exigir um tipo diferente de
tratamento ou recuperação. Ter múltiplos blocos except facilita essa distinção e ação personalizada.
"""
