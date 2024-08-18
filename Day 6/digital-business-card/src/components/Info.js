import pfp from "../images/pfp.jpg"
import "../index.css"

export default function Info(){
    return(
        <div className="Info">
            <img src={pfp} className="ProfilePic"/>
            <h1> Abhiragh A R </h1>
            <h4> Front End Noobie</h4>
            <h6> abhiragh0@gmail.com </h6>
            <div className="Buttons">
                <button id="Email-Button"> <i class="fa fa-envelope"></i> Email </button>
                <button id="Linkedin-Button"> <i class="fa fa-linkedin-square"></i> Linkedin </button>
            </div>
        </div>
    )
}