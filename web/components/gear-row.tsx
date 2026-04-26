import { GearItem } from "@/types";
import { Button } from "./ui/button";
import { SquarePen, Trash} from "lucide-react";

type Props = {
    item: GearItem
    onEdit: (item: GearItem) => void
    onDelete: (id: string) => void
}

export default function GearRow({item, onEdit, onDelete}: Props) {
    return (
        <div>
            {/* TODO: Finish off this component */}
            <span>{item.name}</span>
            <span>{item.weight}</span>

            <Button><SquarePen/></Button>
            <Button><Trash/></Button>
        </div>
    );
}