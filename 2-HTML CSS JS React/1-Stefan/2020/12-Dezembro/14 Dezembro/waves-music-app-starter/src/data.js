import { v4 as uuidv4 } from "uuid";
// music
import porter from "./audio/Porter Robinson - Something Comforting.mp3";
import madeon from "./audio/Madeon - Miracle.mp3";
import doss from "./audio/Doss - Softpretty.mp3";
import cook from "./audio/A. G. Cook - Soft Landing.mp3";
import hakushi from "./audio/Hakushi Hasegawa - hikari.mp3";
import jai from "./audio/Jai Wolf - Telepathy.mp3";
import san from "./audio/San Holo - lift me from the ground.mp3";
import mura from "./audio/Mura Masa, Clairo - I Dont Think I Can Do This Again.mp3";
import paperface from "./audio/PaperFace - Awake.mp3";
import knower from "./audio/KNOWER - overtime.mp3";

const EDM = () => {
    return [
        {
            name: "Something Comforting",
            cover: "https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/a6/22/99/a622998c-c006-e842-2cc7-a110c863645c/jacket_SIXX06268B01A_550.jpg/600x600bf.png",
            artist: "Porter Robinson",
            audio: porter,
            color: ["#639DDD", "#628052", "#4A6E68", "#000000"],
            id: uuidv4(),
            active: true,
        },
        {
            name: "Miracle",
            cover: "https://is3-ssl.mzstatic.com/image/thumb/Music113/v4/de/5c/c4/de5cc49b-1e97-f373-cca0-5d2374332800/886448085232.jpg/600x600bf.png",
            artist: "Madeon",
            audio: madeon,
            color: ["#00F3E9", "#00AFE9", "#DC91D5", "#AC62E5"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "Softpretty",
            cover: "https://rustedbox.com/wp-content/uploads/2014/05/doss.jpg",
            artist: "Doss",
            audio: doss,
            color: ["#fc94c5", "#fba3d4", "#fbacd3", "#f8b4d3"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "Soft Landing",
            cover: "https://cdn.shopify.com/s/files/1/2976/0132/files/unnamed_copy_2_63731ebb-7963-4c15-aae3-42023d632448_grande.jpg?v=1596137114",
            artist: "A. G. Cook",
            audio: cook,
            color: ["#DEDEDE", "#B1B1B1", "#7A7A7A", "#494949"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "hikari",
            cover: "https://base-ec2if.akamaized.net/w=640,a=0,q=90,u=1/images/item/origin/d053fbe8aad744644354cf8c69580be0.jpg",
            artist: "Hakushi Hasegawa",
            audio: hakushi,
            color: ["#948964", "#303C2F", "#2F4D55", "#1c3949"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "Telepathy",
            cover: "https://is3-ssl.mzstatic.com/image/thumb/Music124/v4/18/83/a9/1883a95b-14ef-78b5-4881-f3d5dfe9948c/3Kx3K.jpg/600x600bf.png",
            artist: "Jai Wolf",
            audio: jai,
            color: ["#DA1E22", "#CEA800", "#00C6CD", "#031E2F"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "lift me from the ground",
            cover: "https://is5-ssl.mzstatic.com/image/thumb/Music128/v4/57/00/83/57008363-01a2-5a3a-2df5-d077ea6c92ad/8718857500285.png/600x600bf.png",
            artist: "San Holo",
            audio: san,
            color: ["#F0EFF5", "#CD8F89", "#9C406F", "#38848E"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "I Don’t Think I Can Do This Again",
            cover: "https://media.pitchfork.com/photos/5e18a75ac3431b000823bda3/1:1/w_600/rawyouthcollage.jpg",
            artist: "Mura Masa, Clairo",
            audio: mura,
            color: ["#ac5454", "#b46c6c", "#9b7a71", "#9a847e"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "Awake",
            cover: "https://resources.tidal.com/images/78532ed0/be9c/4645/8ad3/19fd12bf7162/640x640.jpg",
            artist: "PaperFace",
            audio: paperface,
            color: ["#28242c", "#302e2f", "#8c3b0e", "#bc8355"],
            id: uuidv4(),
            active: false,
        },
        {
            name: "overtime",
            cover: "https://img.discogs.com/sBnYSY9PJX-l4spqpBEua7gPOKg=/fit-in/600x600/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-10050278-1490741190-2396.jpeg.jpg",
            artist: "KNOWER",
            audio: knower,
            color: ["#F8E75C", "#5C84BD", "#BD5845", "#010101"],
            id: uuidv4(),
            active: false,
        },
    ]
}

export default EDM;