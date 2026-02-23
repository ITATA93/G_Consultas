# SQLUser.OEC_TextResultSection

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SEC_ParRef | bigint | PK |  | NO | OEC_TextResultType Parent Reference |
| SEC_Childsub | double |  |  | NO | Childsub |
| SEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SEC_ControlType | varchar |  |  | SI | ControlType |
| SEC_CreatedDate | date |  |  | SI | Created Date |
| SEC_CreatedTime | time |  |  | SI | Created Time |
| SEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SEC_Desc | varchar |  |  | NO | Section Name |
| SEC_FontName | varchar |  |  | SI | Font Name |
| SEC_FontSize | varchar |  |  | SI | Font Size |
| SEC_FontStyle | varchar |  |  | SI | Font Style |
| SEC_HTMLTemplate_DR | bigint |  | FK | SI | HTMLTemplate |
| SEC_Order | double |  |  | SI | Order in Printing |
| SEC_RTF | varchar |  |  | SI | RTF |
| SEC_RTFTemplateWEB | varchar |  |  | SI | RTFTemplateWEB |
| SEC_RowId | varchar |  |  | NO | - |
| SEC_UpdatedDate | date |  |  | SI | Updated Date |
| SEC_UpdatedTime | time |  |  | SI | Updated Time |
| SEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SEC_Values | varchar |  |  | SI | Values |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*