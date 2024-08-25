export default function Card(props){
    console.log(props.data)
    return(
        <div className="card">
            <section className="card--left">
                <img src={props.imageUrl} />
            </section>
            <section className="card--right">
                <div className="location--section">
                    <p className="card--location"><i class="fa fa-map-marker"></i> {props.location}</p>
                    <a href={props.googleMapsUrl}>View On Google Maps</a>
                </div>
                <p className="card--title">{props.title}</p>
                <p className="card--dates">{props.startDate} - {props.endDate}</p>
                <p className="card--desc">{props.description}</p>
            </section>
        </div>
    )
}