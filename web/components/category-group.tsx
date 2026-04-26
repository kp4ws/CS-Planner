import { GearItem } from "@/types";
import GearRow from "@/components/gear-row";

type Props = {
  title: string
  items: GearItem[]
  onEdit: (item: GearItem) => void
  onDelete: (id: string) => void
};

export default function CategoryGroup({ title, items, onEdit, onDelete }: Props) {
  return (
    <div>
      {/* CATEGORY NAME */}
      <h2 className="text-emerald-100 font-semibold">{title}</h2>

      {/* CATEGORY ITEMS */}
      <div>
        {items.map((item) => (
          <GearRow 
            key={item.id}
            item={item}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        ))}
      </div>
    </div>
  );
}