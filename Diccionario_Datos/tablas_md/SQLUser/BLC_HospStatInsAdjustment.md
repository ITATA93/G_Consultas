# SQLUser.BLC_HospStatInsAdjustment

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADJ_ParRef | bigint | PK |  | NO | BLC_HospitalStatus Parent Reference |
| ADJ_Childsub | double |  |  | NO | Childsub |
| ADJ_CreatedDate | date |  |  | SI | Created Date |
| ADJ_CreatedTime | time |  |  | SI | Created Time |
| ADJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADJ_DateFrom | date |  |  | SI | Date From |
| ADJ_DateTo | date |  |  | SI | Date To |
| ADJ_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| ADJ_Perc | double |  |  | SI | % Adjustment |
| ADJ_RowId | varchar |  |  | NO | - |
| ADJ_UpdatedDate | date |  |  | SI | Updated Date |
| ADJ_UpdatedTime | time |  |  | SI | Updated Time |
| ADJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ17DR | - |  |  | SI | Child Reference: Registro de modificaciones |
| Q03Q1 | - |  |  | SI | Cuenta con Familiar o Red de Apoyo |
| Q03Q2 | - |  |  | SI | ¿Quién? Nombre Completo |
| Q03Q3 | - |  |  | SI | Rut |
| Q03Q4 | - |  |  | SI | Fecha de Nacimiento |
| Q03Q5 | - |  |  | SI | Estado Civil |
| Q03Q6 | - |  |  | SI | Escolaridad |
| Q03Q7 | - |  |  | SI | Domicilio |
| Q03Q8 | - |  |  | SI | Teléfono |
| Q03Q9 | - |  |  | SI | Tipo de relación o parentesco |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*