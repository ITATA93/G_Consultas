# SQLUser.ARC_InsurAdjustPrice

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IAP_RowId | bigint | PK |  | NO | - |
| ChildQ253DR | - |  |  | SI | Child Reference: Actividades de la Vida Diaria y T... |
| IAP_Adjust | double |  |  | NO | % Adjustment |
| IAP_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| IAP_CreatedDate | date |  |  | SI | Created Date |
| IAP_CreatedTime | time |  |  | SI | Created Time |
| IAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IAP_DateFrom | date |  |  | NO | Date From |
| IAP_DateTo | date |  |  | SI | DateTo |
| IAP_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| IAP_UpdatedDate | date |  |  | SI | Updated Date |
| IAP_UpdatedTime | time |  |  | SI | Updated Time |
| IAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q251Q1 | - |  |  | SI | Evaluación |
| Q251Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*