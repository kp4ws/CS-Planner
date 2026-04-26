export type GearItem = {
    id: string
    name: string
    category: string
    brand?: string
    weight?: number
    weightUnit?: 'lb' | 'oz' | 'kg' | 'g'
    notes?: string
}