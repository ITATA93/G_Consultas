# SQLUser.PA_ORG

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORG_RowID | bigint | PK |  | NO | - |
| ORG_AddrType_DR | bigint |  | FK | SI | Des Ref to CTADR |
| ORG_Blk | varchar |  |  | SI | Block |
| ORG_City_DR | bigint |  | FK | SI | Des Ref to CTCIT |
| ORG_Code | varchar |  |  | NO | Code |
| ORG_Level | varchar |  |  | SI | Level |
| ORG_Name | varchar |  |  | NO | Name |
| ORG_StName | varchar |  |  | SI | Street Name |
| ORG_State_DR | bigint |  | FK | SI | Des Ref to CTSTT |
| ORG_TelO | varchar |  |  | SI | Office Telephone Number |
| ORG_TelOExt | varchar |  |  | SI | Extension No (Ext) |
| ORG_Unit | varchar |  |  | SI | Unit |
| ORG_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*