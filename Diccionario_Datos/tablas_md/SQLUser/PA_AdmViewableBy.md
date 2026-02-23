# SQLUser.PA_AdmViewableBy

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VIEW_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q06Q1 | - |  |  | SI | Date |
| Q06Q2 | - |  |  | SI | Time |
| Q06Q3 | - |  |  | SI | Skin condition |
| Q06Q4 | - |  |  | SI | Other skin condition |
| Q06Q5 | - |  |  | SI | Patch adhesion to skin |
| Q06Q6 | - |  |  | SI | Action taken |
| Q06Q7 | - |  |  | SI | Assessed by |
| Q06Q8 | - |  |  | SI | Assessment notes |
| Q06Q9 | - |  |  | SI | Action taken - Other notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| VIEW_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| VIEW_CareProvType_DR | bigint |  | FK | SI | Des Ref CareProvType |
| VIEW_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| VIEW_Childsub | double |  |  | NO | Childsub |
| VIEW_Comments | varchar |  |  | SI | Comments  |
| VIEW_DateFrom | date |  |  | SI | Date From |
| VIEW_DateTo | date |  |  | SI | Date To |
| VIEW_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*