# SQLUser.ARC_InsTypeGuarGrpNum

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYGU_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| PAYGU_Childsub | double |  |  | NO | Childsub |
| PAYGU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAYGU_CustomerID | varchar |  |  | SI | Customer ID |
| PAYGU_CustomerType | varchar |  |  | SI | Customer Type |
| PAYGU_DateFrom | date |  |  | SI | Date From |
| PAYGU_DateTo | date |  |  | SI | Date To |
| PAYGU_GuarantorGroup_DR | bigint |  | FK | SI | Des Ref ARCGuarantorGroup |
| PAYGU_GuarantorGrpNum | varchar |  |  | SI | Guarantor Group Number |
| PAYGU_RowId | varchar |  |  | NO | - |
| PAYGU_UpdateMode | varchar |  |  | SI | Update Mode |
| Q82Q1 | - |  |  | SI | Hallazgo |
| Q82Q2 | - |  |  | SI | Ubicación |
| Q82Q3 | - |  |  | SI | Sensibilidad |
| Q82Q4 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*