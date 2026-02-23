# SQLUser.ARC_BillSubAgeDepend

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGE_ParRef | varchar | PK |  | NO | ARC_BillSub Parent Reference |
| AGE_AgeFrom | double |  |  | SI | Age From |
| AGE_AgeTo | double |  |  | SI | Age To |
| AGE_Childsub | double |  |  | NO | Childsub |
| AGE_CreatedDate | date |  |  | SI | Created Date |
| AGE_CreatedTime | time |  |  | SI | Created Time |
| AGE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGE_DateFrom | date |  |  | SI | Date From |
| AGE_DateTo | date |  |  | SI | Date To |
| AGE_FixedAmt | double |  |  | SI | Fixed Amt |
| AGE_Injection | varchar |  |  | SI | Injection |
| AGE_Perc | double |  |  | SI | % Charge |
| AGE_RowId | varchar |  |  | NO | - |
| AGE_UpdatedDate | date |  |  | SI | Updated Date |
| AGE_UpdatedTime | time |  |  | SI | Updated Time |
| AGE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| AGE_VisitType | varchar |  |  | SI | Visit Type |
| Q02Q1 | - |  |  | SI | Insumo |
| Q02Q2 | - |  |  | SI | Proveedor |
| Q02Q3 | - |  |  | SI | Cantidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*