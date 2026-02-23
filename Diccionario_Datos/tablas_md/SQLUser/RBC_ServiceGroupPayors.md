# SQLUser.RBC_ServiceGroupPayors

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAY_ParREf | bigint | PK |  | NO | RBC_ServiceGroup Parent Reference |
| PAY_Childsub | double |  |  | NO | Childsub |
| PAY_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAY_CreatedDate | date |  |  | SI | Created Date |
| PAY_CreatedTime | time |  |  | SI | Created Time |
| PAY_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAY_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PAY_MaxDays | double |  |  | SI | Maximum Days |
| PAY_RowId | varchar |  |  | NO | - |
| PAY_UpdatedDate | date |  |  | SI | Updated Date |
| PAY_UpdatedTime | time |  |  | SI | Updated Time |
| PAY_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*