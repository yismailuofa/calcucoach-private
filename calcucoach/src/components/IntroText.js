import StartButton from "./StartButton";

export default function IntroText(props) {
  return (
    <div
      style={{
        fontSize: "5vh",
        // backgroundColor: "#4a86ba",
        background: "linear-gradient(135deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
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
      <StartButton/> 
    </div>
  );
}
