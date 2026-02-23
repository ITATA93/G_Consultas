# SQLUser.ARC_ItemCareProvProportion

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPPROP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| CPPROP_ChargeCode | varchar |  |  | SI | Charge Code |
| CPPROP_Childsub | double |  |  | NO | Childsub |
| CPPROP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPPROP_CreatedDate | date |  |  | SI | Created Date |
| CPPROP_CreatedTime | time |  |  | SI | Created Time |
| CPPROP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPPROP_DateFrom | date |  |  | NO | Date From |
| CPPROP_DateTo | date |  |  | SI | Date To |
| CPPROP_FixedAmount | double |  |  | SI | Fixed Amount |
| CPPROP_Hospital_DR | bigint |  | FK | SI | Des Ref to CTHospital |
| CPPROP_InsuranceType_DR | bigint |  | FK | SI | Des Ref to ARCInsuranceType |
| CPPROP_PayorGroup_DR | bigint |  | FK | SI | Des Ref PayorGroup |
| CPPROP_Percentage | double |  |  | SI | Percentage |
| CPPROP_Rank | integer |  |  | SI | Rank |
| CPPROP_RowId | varchar |  |  | NO | - |
| CPPROP_UpdatedDate | date |  |  | SI | Updated Date |
| CPPROP_UpdatedTime | time |  |  | SI | Updated Time |
| CPPROP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ73DR | - |  |  | SI | Child Reference: Oculomotilidad |
| Q165Q1 | - |  |  | SI | No Usar |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*