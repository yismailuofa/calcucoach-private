import StartButton from "./StartButton";

export default function IntroText(props) {
  return (
    <div
      style={{
        fontSize: "5vh",
        backgroundColor: "#4a86ba",
        padding: "4vh",
        paddingTop: "2vh",
        marginTop: "-4vh",
        borderRadius: "4vh",
        display: "flex",
        flexDirection: "column",
        position: "relative",
        justifyText: "center",
        boxShadow: "0vw 5px 20px black",
      }}
    >
      Free training.<br/>Made for you.
      <StartButton prev={props.prevStep}/> 
    </div>
  );
}
