from PIL import Image
import streamlit as st

st.set_page_config(page_title='Aspects Webpage', page_icon=':robot:', layout='wide')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

img_contact_form= Image.open('images/welcomephilippines.jpg')
boracay= Image.open('images/boracay.jpg')
banaue= Image.open('images/banaue.JPG')
davao= Image.open('images/davao.jpg')
coron= Image.open('images/coron.jpg')
puerto= Image.open('images/puerto.jpg')



with st.container():
    st.title('------------------------------Welcome to my Webpage------------------------------')
with st.container():
    column1, column2, column3 = st.columns((1, 1.1, 1))
    with column2:
     st.subheader('-----------------Abou Louie------------------')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
      st.header('Programming Project')
      st.write('####')
      st.write('Make Webpage using Streamlit')
      st.write('Then Host your [Streamlit](https://streamlit.io/) app on [Github](https://github.com/)')
      st.write('[Click Here for Tutorial](https://blog.streamlit.io/host-your-streamlit-app-for-free/)')
    with right_column:
        st.empty()

with st.container():
    st.write('###')
    st.write('###')
    st.write('---')
with st.container():
     left, center, right = st.columns((0.8,2,0.8))
     with center:
         st.title('Best Places to visit in the Philippines')

with st.container():
    column, column2, colum = st.columns((0.01, 2, 0.01))
    with column2:
      st.write('###')
      st.image(img_contact_form, width= 1350)
    with colum:
        st.empty()
    with column:
        st.empty()

with st.container():
    st.write('---')
    st.header('Boracay')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(boracay)
    with text_column:
        st.subheader('Boracay')
        st.write(
            """Boracay, a popular Philippine destination, attracts visitors with its stunning White Beach, offering 
            powdery white sand and clear waters. The island boasts a variety of water activities, vibrant nightlife, 
            and breathtaking sunsets. With diverse cuisine, friendly locals, and opportunities for relaxation and 
            wellness, Boracay provides a well-rounded and enjoyable experience for tourists. Island hopping, exploring 
            nearby attractions like Apo Reef Natural Park, and participating in festivals add to the island's allure. 
            It's important to stay informed about any changes in travel conditions and the status of the destination.
            """
        )
        st.markdown('[Learn more...](https://guidetothephilippines.ph/articles/ultimate-guides/boracay-travel-guide)')

with st.container():
    st.write('##')
    st.header('Banaue')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(banaue)
    with text_column:
        st.subheader('Banaue')
        st.write(
            """Banaue, Philippines, is renowned for its captivating rice terraces, often referred to as the "Eighth 
            Wonder of the World." Visitors are drawn to the breathtaking landscape, rich cultural heritage, and 
            opportunities for trekking and exploring indigenous villages. The terraces showcase remarkable engineering 
            by the Ifugao people and offer a unique cultural and natural experience.
        """
        )
        st.markdown('[Learn more...](https://www.banaue.gov.ph/)')

with st.container():
    st.write('##')
    st.header('Davao City')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(davao)
    with text_column:
        st.subheader ('Davao City')
        st.write(
            """Davao City beckons visitors with its unique offerings, from tasting the infamous durian fruit and 
            exploring Mt. Apo to experiencing cultural diversity, visiting the Philippine Eagle Center, and enjoying the
             clean, safe environment, making it a compelling destination in Mindanao.
            """
        )
        st.markdown('[Learn more...](https://www.detourista.com/guide/davao-attractions/)')

with st.container():
    st.write('##')
    st.header('Coron Island')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(coron)
    with text_column:
        st.subheader ('Coron Island')
        st.write(
            """One of the top diving destinations in the world, Coron Island is a tropical paradise, with electric blue 
            and green water that almost seems unreal. The mountainous island sits on the tip of the Palawan island 
            region, the western-most section of islands in the Philippines.

The island is popular for diving because of the numerous wrecks here. Many of the preserved shipwrecks are located in 
depths ranging from shallow water at just three meters to deep water at 42 meters.
            """
        )
        st.markdown('[Learn more...](https://www.getyourguide.com/-l105241/-tc172/?cmp=bing&ad_id=77721933411040&adgroup_id=1243548300742209&bid_match_type=bb&campaign_id=710116968&device=c&feed_item_id=&keyword=location_id%3D105241&loc_interest_ms=149&loc_physical_ms=152985&match_type=b&msclkid=7b6f9edac469173ad404fbaf5831aebb&network=o&partner_id=CD951&target_id=dat-2329521542124737:aud-806259112&utm_adgroup=lc%3D105241%3Acoron%7Cfn%3Df1%7Cagt%3Ddsa&utm_campaign=dc%3D65%3Aph%7Clc%3D105241%3Acoron%7Cct%3Dcore%7Cln%3D29%3Aen%7Ctc%3Dall&utm_keyword=location_id%3D105241&utm_medium=paid_search&utm_query=coron%20island&utm_source=bing)')

with st.container():
    st.write('##')
    st.header('Puerto Princesa')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(puerto)
    with text_column:
        st.subheader ('Puerto Princesa')
        st.write(
            """The rock islands, caves, and natural parks of Palawan Island are the hidden paradise of the Philippines. 
            The coastal city of Puerto Princesa is where you should base yourself in order to explore some of these 
            natural gems of the country.

The Subterranean River National Park is a great first stop to see a five-mile underground river and impressive limestone 
caves. The UNESCO World Heritage site has boat tours that take you through the national park.
        """
                 )
        st.markdown('[Learn more...](https://www.traveltothephilippines.info/2020/07/05/buenavista-cave-amazing-stone-formation/)')

with st.container():
    st.write('---')
    st.header('Get in Touch with me!')
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/beboyimba30@email.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email"placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
</form>
"""
    left_column, mid_column, right_column = st.columns((2, 2 , 2))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    with mid_column:
        st.empty()
