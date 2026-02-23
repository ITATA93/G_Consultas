# SQLUser.PHC_PrescriptionNumbers

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESC_Date1 | date | PK |  | NO | - |
| PRESC_CreatedDate | date |  |  | SI | Created Date |
| PRESC_CreatedTime | time |  |  | SI | Created Time |
| PRESC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRESC_Date | date |  |  | NO | Rowid |
| PRESC_Number | double |  |  | SI | The Prescription number counter for the day |
| PRESC_UpdatedDate | date |  |  | SI | Updated Date |
| PRESC_UpdatedTime | time |  |  | SI | Updated Time |
| PRESC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*