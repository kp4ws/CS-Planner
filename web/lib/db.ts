import Dexie, { type Table } from "dexie";
import { GearItem, Trip, TripItem, Category } from "@/types";

export class BackpackPalDB extends Dexie {
    gear_items!: Table<GearItem>;
    trips!: Table<Trip>;
    trip_items!: Table<TripItem>;
    categories!: Table<Category>;

    // TODO: Need to finish filling out the constructor
    constructor() {
        super('BackpackPalDB');
        this.version(1).stores({
            gear_items: '++id, name, category_id',
            trips: '',
            trip_items: '',
            categories: '',
        })
    }
};

export const db = new BackpackPalDB();