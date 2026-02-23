# SQLUser.ARC_AdmixtureRecDoseEquiv

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RECDE_ParRef | bigint | PK |  | NO | ARCAdmixtureRec Parent Reference |
| ChildQ30DR | - |  |  | SI | Child Reference: Prótesis Dental |
| Q29Q1 | - |  |  | SI | Vestido |
| Q29Q10 | - |  |  | SI | Bolso |
| Q29Q2 | - |  |  | SI | Abrigo |
| Q29Q3 | - |  |  | SI | Sweater |
| Q29Q4 | - |  |  | SI | Camisa |
| Q29Q5 | - |  |  | SI | Blusa |
| Q29Q6 | - |  |  | SI | Cinturón |
| Q29Q7 | - |  |  | SI | Corbata |
| Q29Q8 | - |  |  | SI | Cartera |
| Q29Q9 | - |  |  | SI | Mochila |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RECDE_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| RECDE_Childsub | double |  |  | NO | Childsub |
| RECDE_CreatedDate | date |  |  | SI | Created Date |
| RECDE_CreatedTime | time |  |  | SI | Created Time |
| RECDE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RECDE_DefaultDose | double |  |  | SI | Default Dose |
| RECDE_Qty | double |  |  | SI | Quantity |
| RECDE_RowId | varchar |  |  | NO | - |
| RECDE_UpdatedDate | date |  |  | SI | Updated Date |
| RECDE_UpdatedTime | time |  |  | SI | Updated Time |
| RECDE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*