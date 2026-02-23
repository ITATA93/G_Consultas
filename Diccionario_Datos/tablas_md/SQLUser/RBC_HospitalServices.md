# SQLUser.RBC_HospitalServices

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HSER_RowId | bigint | PK |  | NO | - |
| HSER_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| HSER_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| HSER_Active | varchar |  |  | SI | Active |
| HSER_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| HSER_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| HSER_CreatedDate | date |  |  | SI | Created Date |
| HSER_CreatedTime | time |  |  | SI | Created Time |
| HSER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HSER_Desc | varchar |  |  | SI | Description |
| HSER_Equip_DR | bigint |  | FK | SI | Des Ref Equip |
| HSER_Minutes | double |  |  | SI | Minutes |
| HSER_NoOfSlots | double |  |  | SI | No Of Slots |
| HSER_ServGroup_DR | bigint |  | FK | SI | Des Ref ServGroup |
| HSER_Services_DR | bigint |  | FK | SI | Des Ref RBC Services |
| HSER_UpdatedDate | date |  |  | SI | Updated Date |
| HSER_UpdatedTime | time |  |  | SI | Updated Time |
| HSER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*