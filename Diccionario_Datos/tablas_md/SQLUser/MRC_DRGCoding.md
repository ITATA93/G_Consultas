# SQLUser.MRC_DRGCoding

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGCOD_RowId | bigint | PK |  | NO | - |
| ChildQ58DR | - |  |  | SI | Child Reference: Abdomen y dorso |
| DRGCOD_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DRGCOD_Code | varchar |  |  | NO | Code |
| DRGCOD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGCOD_CreatedDate | date |  |  | SI | Created Date |
| DRGCOD_CreatedTime | time |  |  | SI | Created Time |
| DRGCOD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGCOD_DRG_DR | bigint |  | FK | SI | Des Ref DRG |
| DRGCOD_DateFrom | date |  |  | SI | Date From |
| DRGCOD_DateTo | date |  |  | SI | Date To |
| DRGCOD_Desc | varchar |  |  | NO | Description |
| DRGCOD_FollowUpReasonDR | bigint |  | FK | SI | Follow Up Reason DR |
| DRGCOD_HospitalCT_DR | bigint |  | FK | SI | Hospital CT des ref |
| DRGCOD_OnOff | varchar |  |  | SI | On Off |
| DRGCOD_Owner | varchar |  |  | SI | Owner |
| DRGCOD_UpdatedDate | date |  |  | SI | Updated Date |
| DRGCOD_UpdatedTime | time |  |  | SI | Updated Time |
| DRGCOD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q51Q1 | - |  |  | SI | Percusión |
| Q51Q2 | - |  |  | SI | Auscultación |
| Q51Q3 | - |  |  | SI | Localización |
| Q51Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*