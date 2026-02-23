# SQLUser.OR_AnaestAncCareEquip

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAACE_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAACE_Childsub | double |  |  | NO | Childsub |
| ANAACE_RowId | varchar |  |  | NO | - |
| ANAACE_Type_DR | bigint |  | FK | SI | Des Ref User.ORCAncillaryCareEquipment |
| Q18Q1 | - |  |  | SI | Assessment date |
| Q18Q2 | - |  |  | SI | Assessment time |
| Q18Q3 | - |  |  | SI | Insertion site check |
| Q18Q4 | - |  |  | SI | Tube checks |
| Q18Q5 | - |  |  | SI | Actions performed |
| Q18Q6 | - |  |  | SI | Assessment notes |
| Q18Q7 | - |  |  | SI | Assessed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*