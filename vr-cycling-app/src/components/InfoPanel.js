import React from 'react';
import './InfoPanel.css';

function InfoPanel() {
  return (
    <div className="info-panel">
      <div className="info-section">
        <div className="info-card">
          <p>
            <font size = "3"><b> VR Cycling </b> offers an immersive real-world riding experience, 
            allowing you to pedal freely through realistic 360° environments. 
            It effectively bridges the gap between virtual simulation and real-world cycling.</font>
          </p>
        </div>
        <div className="info-card">
          <p>
            <font size = "3"><b> VR cycling </b> ඔබට සජීවීකරණයකින් ඔබ්බට ගිය, 360° පරිසරයන් හරහා නිදහසේ සයිකල් පැදීමේ අත්දැකීමක් ලබා දෙයි. 
            මෙමගින් පරිගණක මගින් නිර්මාණය කරන ලද අනුකරණවල සහ ස්වභාවික ලෝකයේ සයිකල් පැදීම අතර ඇති පරතරය කාර්යක්ෂමව පුරවා දේ.</font>
          </p>
        </div>
        <div className="info-card">
          <p>
            <font size = "3"><b> VR Cycling </b> </font> <font size = "2"> உங்களுக்கு உண்மையான சைக்கிள் சவாரி போன்ற
               அனுபவத்தை வழங்கும் ஒரு மெய்நிகர் நடைமுறை. 360° சூழல்களில் முழு சுதந்திரத்துடன் சைக்கிள்
                ஓட்ட அனுமதிப்பதன் மூலம், இது மெய்நிகர் உருவகமும் நிஜ உலக சவாரி அனுபவமும் இடையிலான
                 இடைவெளியை திறம்பட இணைக்கிறது</font>
          </p>
        </div>
      </div>
    </div>
  );
}

export default InfoPanel;
