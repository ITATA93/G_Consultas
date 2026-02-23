# SQLUser.MRC_DRGCodesWeight

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WGHT_ParRef | bigint | PK |  | NO | MRC_DRGCodes Parent Reference |
| ChildQ51DR | - |  |  | SI | Child Reference: Pulmón |
| Q36Q1 | - |  |  | SI | Hallazgos |
| Q36Q2 | - |  |  | SI | Ubicación |
| Q36Q3 | - |  |  | SI | Lateralidad |
| Q36Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WGHT_Childsub | double |  |  | NO | Childsub |
| WGHT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WGHT_CreatedDate | date |  |  | SI | Created Date |
| WGHT_CreatedTime | time |  |  | SI | Created Time |
| WGHT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WGHT_DateFrom | date |  |  | SI | Date From |
| WGHT_DateTo | date |  |  | SI | Date To |
| WGHT_HCPCsPortion | double |  |  | SI | HCPCs Portion |
| WGHT_PharmacyPortion | double |  |  | SI | Pharmacy Portion % |
| WGHT_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| WGHT_RowId | varchar |  |  | NO | - |
| WGHT_SurgHighCostPortion | double |  |  | SI | Surgical High Cost Portion % |
| WGHT_UpdatedDate | date |  |  | SI | Updated Date |
| WGHT_UpdatedTime | time |  |  | SI | Updated Time |
| WGHT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WGHT_Weight | double |  |  | SI | Weight |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*