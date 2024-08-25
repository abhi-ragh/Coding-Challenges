import Nav from "./components/Nav";
import Card from "./components/Card";
import data from "./data";

export default function App(){
    const item = data.map( x => {
        return <Card 
            {... x}
        />
    })
    return(
        <>
            <Nav />
            {item}
        </>
    )
}