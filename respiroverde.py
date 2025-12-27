import streamlit as st

html_code = """
<body>
    <div style="background-color:#425C00;">
        <header style="display:flex;justify-content:space-between;">
            <nav style="display:flex;justify-content:space-between;color:#E9F9B2;gap:2px;">
                <ul style="display:flex;justify-content:space-between;gap:2rem;align-items:center;margin:2rem;font-size:1.5em;list-style:none;">
                    <li><a href="#" style="color:#E9F9B2;text-decoration-line:none;">Inicio </a></li>
                    <li><a href="#" style="color:#E9F9B2;text-decoration-line:none;">Sobre nós</a></li>
                </ul>
            </nav>
        </header>
    </div>
    <div style="background-color:#E9F9B2;">
        <h1 style="font-size:3rem;text-align:center;text-transform:uppercase;color:#425C00;">A importância da luz para as plantas</h1>
	<p style="font-size:1.5rem;text-align:justify;color:#425C00;margin:2rem;">
                    Fotossíntese: A luz é essencial para a fotossíntese, o processo pelo qual as plantas convertem a luz solar em energia química. 
                    Durante a fotossíntese, as plantas absorvem dióxido de carbono (CO2) do ar e água do solo, 
                    utilizando a luz para transformar esses elementos em glicose (açúcar) e oxigênio (O2).
        </p>
        <p style="font-size:1.5rem;text-align:justify;color:#425C00;margin:2rem;">
                    Proporciona conforto e bem-estar: Um jardim pode criar um ambiente relaxante e refrescante, 
                    ideal para momentos de descontração.
        </p>
        <p style="font-size:1.5rem;text-align:justify;color:#425C00;margin:2rem">
                    Melhora a decoração: Plantas podem adicionar um toque natural à decoração do apartamento, 
                    criando um ambiente mais harmonioso.
        </p>
        <p style="font-size:1.5rem;text-align:justify;color:#425C00;margin:2rem">
                    Cria um espaço funcional: Um jardim pode ser utilizado para refeições, relaxamento ou simplesmente para apreciar a natureza.
        </p>
    </div>
    <div style="background-color:#425C00;">
        <h1 style="font-size:3rem;text-align:center;text-transform:uppercase;color:#FFFFFF; margin:2rem; margin-top:0rem">Diferentes tipos de necessidade de luz?</h1>
        <p style="font-size:1.5rem;text-align:justify;color:#FFFFFF;margin:2rem;">
                    Plantas que necessitam de sol direto: Preferem várias horas de luz intensa ao dia, como cactos e suculentas. 
	Eles prosperam sob luz forte e podem sofrer com falta de luminosidade.
        </p>
	<p style="font-size:1.5rem;text-align:justify;color:#FFFFFF;margin:2rem;">
                    Plantas que preferem sol parcial: Desenvolvem-se melhor com luz filtrada ou meia-sombra, como samambaias e lírios-da-paz. 
	Eles apreciam luminosidade, mas não toleram longos períodos de exposição direta.
        </p>
	<p style="font-size:1.5rem;text-align:justify;color:#FFFFFF;margin:2rem;">
               Plantas que necessitam de luz indireta: Preferem luz filtrada, como em ambientes com cortinas ou reflexos. Eles não toleram sol intenso e são benéficos em ambientes com luminosidade moderada. 
        </p>
	<p style="font-size:1.5rem;text-align:justify;color:#FFFFFF;margin:2rem;">  Plantas que necessitam de luz difusa: Preferem luz suave e uniforme, como em dias nublados. Eles são beneficiados por ambientes com luminosidade moderada.
     </p>
    </div>
</body>
"""


st.markdown(html_code, unsafe_allow_html=True)
