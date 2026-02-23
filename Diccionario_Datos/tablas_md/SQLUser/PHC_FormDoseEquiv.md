# SQLUser.PHC_FormDoseEquiv

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQ_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| EQ_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| EQ_Childsub | double |  |  | NO | Childsub |
| EQ_CreatedDate | date |  |  | SI | Created Date |
| EQ_CreatedTime | time |  |  | SI | Created Time |
| EQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EQ_DefaultDose | double |  |  | SI | Default Dose |
| EQ_NotAllowPrescBaseUOM | varchar |  |  | SI | Not Allowed to Prescribe in UOM |
| EQ_Qty | double |  |  | SI | Quantity |
| EQ_RowId | varchar |  |  | NO | - |
| EQ_UpdatedDate | date |  |  | SI | Updated Date |
| EQ_UpdatedTime | time |  |  | SI | Updated Time |
| EQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*