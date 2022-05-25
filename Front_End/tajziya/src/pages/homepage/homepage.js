import { useState } from "react";
import { Stack } from "react-bootstrap";
import Cluster from "../../components/cluster";
import Header from "../../components/header";
import Tab from "../../components/tab";
import TagCloudPage from "../../components/tagcloud";
import Help from "../../components/help";
import Media from "../../components/media";

const HomePage = () => {
    const [selectedTab, setSelectedTab] = useState("cluster");
    const [fetchData, setFetchData] = useState(false);
    const [clusterLabelColor, setClusterLabelColor] = useState([]);

    return (
        <Stack className="h-100">
            <Header></Header>

            <Tab setSelectedTab={setSelectedTab}></Tab>
            <div className={selectedTab === "media" ? "flex-grow-1 overflow-hidden" : "flex-grow-1 overflow-auto"}>
                <Cluster display={selectedTab === "cluster"} setFetchData={setFetchData} setClusterLabelColor={setClusterLabelColor}></Cluster>
                <TagCloudPage display={selectedTab === "tagcloud"} fetchData={fetchData} clusterLabelColor={clusterLabelColor}></TagCloudPage>
                <Media display={selectedTab === "media"} fetchData={fetchData} clusterLabelColor={clusterLabelColor}></Media>
                <Help display={selectedTab === "help"}></Help>
            </div>
        </Stack>
    );
};

export default HomePage;
