import StartButton from "./StartButton";

export default function StartText({nextStep}) {
  return (
    <div
      style={{
        fontSize: "5vh",
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
        transform: "translateX(-100vw)",
        transition: "transform .5s cubic-bezier(0.11, 0, 0.5, 0)" // ease In Quad
        // transition: "transform .5s cubic-bezier(0.5, 1, 0.89, 1)" // ease Out Quad
      }}
    >
      Free training.<br/>Made for you.
      <StartButton nextStep={nextStep}/> 
    </div>
  );
}
