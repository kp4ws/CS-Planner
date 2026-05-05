import { GearItem } from "@/types/types";
import GearRow from "@/components/gear-row";

type Props = {
  title: string;
  items: GearItem[];
  onEdit: (item: GearItem) => void;
  onDelete: (id: string) => void;
};

export default function CategoryGroup({
  title,
  items,
  onEdit,
  onDelete,
}: Props) {
  return (
    <div>
      {/* CATEGORY HEADER */}
      <div className="bg-green-700 flex justify-between items-center gap-8 p-3 m-3">
        <h2 className=" text-white font-semibold">{title}</h2>
        <p className="text-sm text-gray-300">{items.length} Items</p>
      </div>

      {/* CATEGORY ITEMS */}
      <div>
        {/* If no items, then display no items. Else display all items for the category group */}
        {items.length === 0 && <p className="text-gray-200 italic">No Items Yet</p>}

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
